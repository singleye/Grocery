var path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'bundle.js',
        path: path.join(__dirname, '/dist'),
    },
    resolve: {
        extensions: ['', '.js', '.jsx']
    },
    module: {
        loaders: {
            { test: /\.jsx?$/, loaders: ['babel'] }
        }
    }
}
