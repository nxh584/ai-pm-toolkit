import chalk from 'chalk';

export function formatMarkdown(content) {
  const lines = content.split(/\r?\n/);
  const output = [];
  let inCodeBlock = false;

  for (const raw of lines) {
    const line = raw ?? '';

    if (line.trim().startsWith('```')) {
      inCodeBlock = !inCodeBlock;
      continue;
    }

    if (inCodeBlock) {
      output.push(chalk.gray(`    ${line}`));
      continue;
    }

    if (/^###\s+/.test(line)) {
      output.push(chalk.bold.cyan(line.replace(/^###\s+/, '')));
      continue;
    }

    if (/^##\s+/.test(line)) {
      output.push(chalk.bold.blue(line.replace(/^##\s+/, '')));
      continue;
    }

    if (/^#\s+/.test(line)) {
      output.push(chalk.bold.green(line.replace(/^#\s+/, '')));
      continue;
    }

    const emphasised = line.replace(/\*\*(.+?)\*\*/g, (_, text) => chalk.bold(text));
    output.push(emphasised);
  }

  return output.join('\n').replace(/\n{3,}/g, '\n\n').trimEnd();
}

export function formatList(items) {
  if (!items.length) {
    return chalk.yellow('No items found.');
  }

  const grouped = items.reduce((acc, item) => {
    const key = item.section || 'general';
    if (!acc[key]) {
      acc[key] = [];
    }
    acc[key].push(item);
    return acc;
  }, {});

  const lines = [];
  for (const section of Object.keys(grouped).sort()) {
    lines.push(chalk.bold.blue(section));
    for (const item of grouped[section]) {
      const desc = item.description || 'No description available.';
      lines.push(`  ${chalk.green('-')} ${chalk.bold(item.name)}: ${desc}`);
    }
    lines.push('');
  }

  return lines.join('\n').trimEnd();
}

export function formatSearchResults(results, query) {
  if (!results.length) {
    return chalk.yellow(`No matches found for "${query}".`);
  }

  const needle = query.toLowerCase();
  const highlight = (value) => {
    const lower = value.toLowerCase();
    const index = lower.indexOf(needle);
    if (index === -1) {
      return value;
    }

    const before = value.slice(0, index);
    const match = value.slice(index, index + query.length);
    const after = value.slice(index + query.length);
    return `${before}${chalk.bold.yellow(match)}${after}`;
  };

  const lines = [chalk.bold(`Search results for "${query}":`), ''];
  for (const result of results) {
    lines.push(
      `${chalk.cyan(`[${result.section}]`)} ${chalk.bold(highlight(result.name))} - ${highlight(result.description)}`
    );
  }

  return lines.join('\n');
}
