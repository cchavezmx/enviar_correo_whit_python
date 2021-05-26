import express from 'express'

import { PythonShell } from 'python-shell'

const app = express()
const PORT = 3000



app.get("/", (req, res) => {

  let option = {
    args: ['cchavezmx@outlook.com', "Se creo la cotizacion <a href=https://itamx.com/#/checkout/invoice/60aec17a6854b30015908460>OC<a>"]
  }
  
  PythonShell.run("./demo.py", option, function(err, output){
      if(err) console.log(err)

      console.log("Correo enviado")
  })

})



app.listen(PORT, () => {
  console.log(`¡Está Vivo! at port ${PORT} `)
})