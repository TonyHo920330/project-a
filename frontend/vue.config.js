const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: 'all',
    host: '0.0.0.0',
    port: 8080,
    client: {
      webSocketURL: 'wss://0.0.0.0:8080/ws' // 指定安全 WebSocket
    }
  }
})
