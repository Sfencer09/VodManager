import {Client} from 'pg'

const client = new Client({
  user: process.env.POSTGRES_USER,
  host: process.env.POSTGRES_HOST || 'postgres',
  database: process.env.POSTGRES_DB || 'vodmanager',
  password: process.env.POSTGRES_PASSWORD,
  port: parseInt(process.env.POSTGRES_PORT || '5432'),
});

export async function query(text: string, params?: string[]) {
  return client.query(text, params)
}

export async function setupDb({

}: {}): Promise<void> {
  await query('CREATE TABLE IF NOT EXISTS')
}

export async function isDbSetup(): Promise<boolean> {
  const versionSettings = await query('SELECT * FROM settings WHERE name="version"');
  return Promise.resolve(versionSettings.rowCount === 1);
}

