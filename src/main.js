import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)
app.use('/uploads',express.static(_dirname+'/uploads'));

app.mount('#app')
