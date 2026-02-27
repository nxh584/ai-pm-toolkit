import ora from 'ora';

import { fetchDirectory, fetchMarkdownDescription } from '../utils/fetcher.js';
import { formatSearchResults } from '../utils/formatter.js';

const SEARCHABLE_SECTIONS = ['prompts', 'skills', 'workflows', 'commands'];

function scoreResult(name, description, query) {
  const q = query.toLowerCase();
  const n = name.toLowerCase();
  const d = description.toLowerCase();

  if (n === q) {
    return 300;
  }
  if (n.includes(q)) {
    return 200;
  }
  if (d.includes(q)) {
    return 100;
  }
  return 0;
}

async function collectPromptEntries() {
  const promptRoot = await fetchDirectory('prompts');
  const categories = promptRoot
    .filter((entry) => entry.type === 'dir')
    .map((entry) => entry.name)
    .sort();

  const entries = [];
  for (const category of categories) {
    const files = await fetchDirectory(`prompts/${category}`);
    for (const file of files) {
      if (file.type !== 'file' || !file.name.endsWith('.md')) {
        continue;
      }
      entries.push({
        section: `prompts/${category}`,
        path: file.path,
        name: file.name.replace(/\.md$/, ''),
        description: await fetchMarkdownDescription(file.path, 'prompts')
      });
    }
  }

  return entries;
}

async function collectFlatEntries(section) {
  const files = await fetchDirectory(section);
  const entries = [];

  for (const file of files) {
    if (file.type !== 'file' || !file.name.endsWith('.md')) {
      continue;
    }
    if (file.name.toLowerCase() === 'readme.md') {
      continue;
    }

    entries.push({
      section,
      path: file.path,
      name: file.name.replace(/\.md$/, ''),
      description: await fetchMarkdownDescription(file.path, section)
    });
  }

  return entries;
}

export async function runSearch(query) {
  if (!query || !query.trim()) {
    throw new Error('Search query is required. Example: ai-pm-toolkit search "clarify"');
  }

  const term = query.trim();
  const spinner = ora(`Searching toolkit for "${term}"...`).start();

  try {
    const rows = [];
    rows.push(...(await collectPromptEntries()));

    for (const section of SEARCHABLE_SECTIONS.filter((item) => item !== 'prompts')) {
      rows.push(...(await collectFlatEntries(section)));
    }

    const ranked = rows
      .map((row) => ({
        ...row,
        score: scoreResult(row.name, row.description, term)
      }))
      .filter((row) => row.score > 0)
      .sort((a, b) => b.score - a.score || a.name.localeCompare(b.name));

    spinner.succeed(`Search complete.`);
    console.log(formatSearchResults(ranked, term));
  } catch (error) {
    spinner.fail('Search failed.');
    throw error;
  }
}
