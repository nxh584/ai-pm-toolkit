import ora from 'ora';

import { fetchDirectory, fetchMarkdownDescription } from '../utils/fetcher.js';
import { formatList } from '../utils/formatter.js';

const SECTIONS = ['prompts', 'skills', 'workflows', 'templates', 'commands'];

function normaliseSection(section) {
  if (!section) {
    return null;
  }

  const value = section.trim().toLowerCase();
  if (value === 'all' || SECTIONS.includes(value)) {
    return value;
  }

  throw new Error(
    `Unknown section \`${section}\`. Use one of: ${[...SECTIONS, 'all'].join(', ')}`
  );
}

async function listPromptCategory(category) {
  const entries = await fetchDirectory(`prompts/${category}`);
  const files = entries.filter((entry) => entry.type === 'file' && entry.name.endsWith('.md'));

  const rows = [];
  for (const file of files.sort((a, b) => a.name.localeCompare(b.name))) {
    const description = await fetchMarkdownDescription(file.path, 'prompts');
    rows.push({
      section: `prompts/${category}`,
      name: file.name.replace(/\.md$/, ''),
      description
    });
  }

  return rows;
}

async function listFlatSection(section) {
  const entries = await fetchDirectory(section);
  const files = entries.filter((entry) => entry.type === 'file' && entry.name.endsWith('.md'));

  const rows = [];
  for (const file of files.sort((a, b) => a.name.localeCompare(b.name))) {
    if (file.name.toLowerCase() === 'readme.md') {
      continue;
    }

    const description = await fetchMarkdownDescription(file.path, section);
    rows.push({
      section,
      name: file.name.replace(/\.md$/, ''),
      description
    });
  }

  return rows;
}

async function listSection(section) {
  if (section === 'prompts') {
    const promptRoot = await fetchDirectory('prompts');
    const categories = promptRoot
      .filter((entry) => entry.type === 'dir')
      .map((entry) => entry.name)
      .sort();

    const allRows = [];
    for (const category of categories) {
      const rows = await listPromptCategory(category);
      allRows.push(...rows);
    }

    return allRows;
  }

  return listFlatSection(section);
}

function countBySection(items) {
  return items.reduce((acc, item) => {
    const key = item.section.startsWith('prompts/') ? 'prompts' : item.section;
    acc[key] = (acc[key] || 0) + 1;
    return acc;
  }, {});
}

export async function runList(sectionArg) {
  const section = normaliseSection(sectionArg);

  if (!section) {
    const spinner = ora('Fetching toolkit summary...').start();
    try {
      const all = [];
      for (const item of SECTIONS) {
        const rows = await listSection(item);
        all.push(...rows);
      }
      spinner.succeed('Toolkit summary loaded.');

      const counts = countBySection(all);
      console.log('Available toolkit sections:\n');
      for (const key of Object.keys(counts).sort()) {
        console.log(`- ${key}: ${counts[key]} items`);
      }
      console.log('\nRun `ai-pm-toolkit list <section>` for detailed output.');
      console.log(`Sections: ${SECTIONS.join(', ')}`);
      return;
    } catch (error) {
      spinner.fail('Failed to load toolkit summary.');
      throw error;
    }
  }

  if (section === 'all') {
    const spinner = ora('Fetching all toolkit sections...').start();
    try {
      const allRows = [];
      for (const item of SECTIONS) {
        const rows = await listSection(item);
        allRows.push(...rows);
      }
      spinner.succeed('Toolkit listing loaded.');
      console.log(formatList(allRows));
      return;
    } catch (error) {
      spinner.fail('Failed to fetch toolkit sections.');
      throw error;
    }
  }

  const spinner = ora(`Fetching ${section}...`).start();
  try {
    const rows = await listSection(section);
    spinner.succeed(`Loaded ${section}.`);
    console.log(formatList(rows));
  } catch (error) {
    spinner.fail(`Failed to fetch ${section}.`);
    throw error;
  }
}
