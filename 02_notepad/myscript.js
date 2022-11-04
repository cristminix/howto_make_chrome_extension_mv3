const elmNote = document.getElementById("note");
const elmSave = document.getElementById("save");

let note = localStorage["note"];
if(note == null){
	note = "";
}

elmNote.value = note;

elmSave.onclick = ()=>{
	localStorage["note"] = elmNote.value;
	console.log("click")
}