import ora from 'ora';

import { fetchFile } from '../utils/fetcher.js';
import { formatMarkdown } from '../utils/formatter.js';

export async function runGet(path) {
  if (!path) {
    throw new Error('Path is required. Example: ai-pm-toolkit get skills/problem-shaping');
  }

  const spinner = ora(`Fetching ${path}...`).start();
  try {
    const { path: resolvedPath, content } = await fetchFile(path);
    spinner.succeed(`Loaded ${resolvedPath}.`);

    console.log('');
    console.log(formatMarkdown(content));
  } catch (error) {
    spinner.fail(`Failed to fetch ${path}.`);
    throw error;
  }
}
