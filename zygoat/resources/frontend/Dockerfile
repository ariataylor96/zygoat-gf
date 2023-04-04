FROM node:latest

RUN npm install -g npm
RUN npm install -g pnpm

WORKDIR /code

COPY . .

RUN pnpm install
RUN pnpm run build

CMD pnpm run start
