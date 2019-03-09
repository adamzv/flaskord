module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  baseUrl: process.env.NODE_ENV === 'production'
    ? '/'
    : '/'
}