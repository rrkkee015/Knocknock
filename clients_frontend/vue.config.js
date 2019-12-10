module.exports = {
  'transpileDependencies': [
    'vuetify'
  ],
  publicPath: '/',
  devServer: {
    proxy: {
      '/accounts': {
        target: 'http://13.125.93.228/'
      },
      '/stores': {
        target: 'http://13.125.93.228/'
      },
    }
  },
  lintOnSave: false
}
