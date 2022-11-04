console.log("Start");

const elmExec = document.getElementById("exec");

console.log(elmExec);
console.dir(elmExec);

elmExec.onclick = ()=>{
	console.log("Exec onclick");
	let a = 1;
	let b = 2;
	let c = a + b;
	console.log("c",c);
}

console.log("End");