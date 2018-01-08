var webpack = require('webpack');
const path = require('path');
module.exports = {
    entry: {
        'dashboard': './app_dir/static/js/'
    },
    output: {
        path: path.resolve('./app_dir/static/dist'),
        filename: '[name].bundle.js'
    },
    module: {
        loaders: [
            { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
            { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ }
        ]
    },
    plugins: [
            new webpack.DefinePlugin({
                'process.env.NODE_ENV': JSON.stringify('development')
            })
        ],
    target: 'node'
}
