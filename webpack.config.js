const path = require("path")
const { VueLoaderPlugin } = require("vue-loader")
const webpack = require("webpack")
const BundleTracker = require("webpack-bundle-tracker")

module.exports = {
  mode: "development",
  entry: {
    main: "./src/project/frontend/lib/src/index.js"
  },
  output: {
    // NOTE: for client-side
    // path: path.resolve(__dirname, "./public/"),
    // filename: "bundle.js"
    // NOTE: for server-side
    path: path.resolve(__dirname, "./src/project/frontend/lib/public/webpack_bundles/"),
    filename: "[name]-[hash].js",
  },
  devServer: {
    static: {
      directory: path.join(__dirname, "./src/project/frontend/lib/public"),
      watch: true,
    },
  },
  resolve: {
    extensions: [".js", ".vue"],
    alias: {
      vue$: "vue/dist/vue.esm.js"
    }
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["vue-style-loader", "css-loader"]
      },
      {
        test: /\.scss$/,
        use: [
          "vue-style-loader",
          "css-loader",
          "sass-loader",
          {
            loader: "sass-resources-loader",
            options: {
              resources: [
                "./src/project/frontend/lib/src/assets/css/main.scss"
              ]
            }
          }
        ]
      },
      {
        test: /\.vue$/,
        loader: "vue-loader",
        options: {
          loaders: {
            scss: "vue-style-loader!css-loader!sass-loader"
          }
        }
      },
      {
        test: /\.png$/i,
        use: [
          "file-loader"
        ],
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
    new BundleTracker({
      path: __dirname,
      filename: "./src/project/frontend/lib/webpack-stats.json"
    })
  ]
}
