const webpack = require('webpack');

const config = {
    devtool: 'eval-source-map',
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: [".js", ".jsx"]
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query:{
                    presets: ['react','es2015']}
            },
        ]
    },
};
module.exports = config;