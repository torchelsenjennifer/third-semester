import brcrypt from "bcrypt"

const senha = "avenida123"

console.time("tempo");
const salt = brcrypt.genSaltSync(10)//10=numero de voltas para criptografar a senha
const hash = brcrypt.hashSync(senha, salt)
console.timeEnd("tempo");//tempo que leva para criptografar a senha

const verifica = await brcrypt.compare(senha, hash) //verifica se a senha esta correta

const msg = verifica ? "Ok! Senha Correta" : "Erro... Incorreta";

console.log(msg);

console.log(senha);//senha normal
console.log(salt);
console.log(hash); //adicona um hash com a senha para dificultar/ salva no banco
