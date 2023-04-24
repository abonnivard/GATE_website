

let boutonup = document.getElementsByClassName('uparrow')
function up (element){
    element.style.display = 'none'
    let down = document.getElementsByClassName('downarrow')
    for (let k = 0;k<down.length;k++){
        if (down[k].id === element.id){
            down[k].style.display = 'flex'
        }
    }
    let infs = document.getElementsByClassName('inf')
    for (let k = 0;k<infs.length;k++){
        if (infs[k].id === element.id){
            infs[k].style.display = 'flex'
        }
    }
}

let arr = Array.from(boutonup)
arr.forEach((element => element.addEventListener('click', function() { up(element); })))


let boutondown = document.getElementsByClassName('downarrow')

function down(element){
    element.style.display = 'none'
    let up = document.getElementsByClassName('uparrow')
    for (let k = 0;k<up.length;k++){
        if (up[k].id === element.id){
            up[k].style.display = 'flex'
        }
    }
    let infs = document.getElementsByClassName('inf')
    for (let k = 0;k<infs.length;k++){
        if (infs[k].id === element.id){
            console.log(infs[k])
            infs[k].style.display = 'none'

        }
    }
}

let arrdown  = Array.from(boutondown)
arrdown.forEach((element => element.addEventListener('click', function() { down(element); })))
