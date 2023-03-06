FROM node:latest

RUN npm install -g npm
RUN npm install -g pnpm

WORKDIR /code

ADD package.json /code/
ADD pnpm-lock.yaml /code/

RUN pnpm install
RUN pnpm run build

CMD pnpm run start
