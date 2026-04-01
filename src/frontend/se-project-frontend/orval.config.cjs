module.exports = {
     default: {
          input: {
               target: 'http://127.0.0.1:8000/openapi.json'
          },
          output: {
               target: './src/lib/api/gen',
               client: 'axios',
               mode: 'split',
               clean: true,
               baseUrl: "http://127.0.0.1:8000"
          }
     }
}