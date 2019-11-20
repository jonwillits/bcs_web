# Brain and Cognitive Science Web

## Development

First, clone the repository to your machine.

### Setting up JavaScript environment

Install `node.js` if you have not already.
On Ubuntu, you can:
```bash
sudo apt install nodejs npm
```
Next, move to the static directory in `src/static`.
Then, create a new `node.js` environment and install dependencies:
```bash
npm init
 npm install --save-dev webpack && npm install -D webpack-cli
npm install --save-dev babel-core babel-loader babel-preset-es2015 babel-preset-react
npm install babel-loader@^7 --save-dev
npm i react react-dom react-router-dom --save-dev
npm i react-d3-tree
```
You are done!
Now, you can make changes and view them in the browser, after running:
```bash
npm run watch
```



