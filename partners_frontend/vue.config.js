module.exports = {
  'transpileDependencies': [
    'vuetify'
  ],
  publicPath: '/',
  devServer: {
    proxy: {
      '/accounts': {
        // target: 'http://localhost:8000/'
        target: 'http://13.125.93.228/'
      },
      '/partner/stores': {
        // target: 'http://localhost:8000/'
        target: 'http://13.125.93.228/'
      },
      '/stores': {
        // target: 'http://localhost:8000/'
        target: 'http://13.125.93.228'
      }
    }
  },
  lintOnSave: false
}
