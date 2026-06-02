import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react' // o @vitejs/plugin-react según la versión instalada
import path from 'path'

export default defineConfig({
  plugins: [react()],
  build: {
    // Ruta archivos compilados
    outDir: path.resolve(__dirname, '../static/react'),
    emptyOutDir: true,
    // Configuración de la ruta de los paquetes react
    rollupOptions: {
      input: {
        // Crear punto de entrada para cada componente asíncrono
        tracker: path.resolve(__dirname, 'src/react-modules/tracker.jsx'),
        catalog: path.resolve(__dirname, 'src/react-modules/catalog.jsx'),
        orders: path.resolve(__dirname, 'src/react-modules/ordersDashboard.jsx'),
      },
      output: {
        // Forzamos nombres sin hashes aleatorios
        entryFileNames: '[name].js',
        assetFileNames: '[name].[ext]',
        chunkFileNames: '[name].js',
      }
    }
  }
})