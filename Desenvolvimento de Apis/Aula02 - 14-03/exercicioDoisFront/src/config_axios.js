import axios from 'axios'

// variável com url do servidor
export const webServiceURL = 'http://localhost:3000/'

export const inAxios=axios.create({baseURL: webServiceURL})