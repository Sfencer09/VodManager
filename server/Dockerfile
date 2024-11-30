# -------- Base Stage --------
FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./
ENV NODE_ENV=production

# -------- Dependencies --------
FROM base AS deps
RUN npm ci

# -------- Development --------
FROM deps AS development
ENV NODE_ENV=development
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0"]

# -------- Build --------
FROM base AS build
ENV NODE_ENV=development
RUN npm install
COPY . .
RUN npm run build

# -------- Production --------
FROM node:20-alpine AS production
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/.next ./.next
COPY --from=build /app/public ./public
COPY --from=build /app/package.json ./package.json
USER node
ENV NODE_ENV=production
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 CMD wget --no-verbose --tries=1 --spider http://localhost:3000/ || exit 1
CMD ["npm", "start"]