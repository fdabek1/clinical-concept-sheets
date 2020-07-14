module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/clinical-concept-sheets/'
    : '/'
}