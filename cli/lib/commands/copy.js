import clipboard from 'clipboardy';
import ora from 'ora';

import { fetchFile } from '../utils/fetcher.js';

export async function runCopy(path) {
  if (!path) {
    throw new Error('Path is required. Example: ai-pm-toolkit copy prompts/problem-shaping/clarify-ambiguity');
  }

  const spinner = ora(`Fetching ${path}...`).start();
  try {
    const { path: resolvedPath, content } = await fetchFile(path);
    await clipboard.write(content);
    spinner.succeed(`Copied ${resolvedPath}.`);

    const displayPath = resolvedPath.replace(/\.md$/, '');
    console.log(
      `✓ Copied ${displayPath} to clipboard. Paste into your agent session.`
    );
  } catch (error) {
    spinner.fail(`Failed to copy ${path}.`);
    throw error;
  }
}
