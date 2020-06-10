module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/ehr-code-mappings/'
    : '/'
}