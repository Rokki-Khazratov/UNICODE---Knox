componentIndex = -1;
randomId = -1
divNum = 0;


function allowDrop(ev) { ev.preventDefault() }
function drag(ev) { ev.dataTransfer.setData('text', ev.target.id) }

function del(elem1, elem2){
  document.getElementById(elem1).remove();
  document.getElementById(elem2).remove();
}

function drop(ev, thiss) {
  ev.preventDefault()
  var data = ev.dataTransfer.getData('text')
  const list = document.getElementById(thiss.id)
  const list1 = document.getElementById(data)

  if (list1.getAttribute('draggable') == 'true') {
    componentIndex += 1;

    const dropper = document.getElementById('dropper').outerHTML
    document.getElementById('dropper').remove()
    const list2 = document.getElementById(thiss.id)
    const canvasZone = document.getElementById('canvasZone')
    const d = new Date();
    const hashIndexId = CryptoJS.MD5("" + d + componentIndex);



    // ________________________________________________________________

    buttonEdit = `<span id="removed" style="z-index: 2; left:64%;" class="position-absolute top-25 translate-middle badge">
      <button class="py-0 h6 px-5 rounded-pill btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#modal`+ hashIndexId + `" aria-controls="offcanvasExample">Edit</button>
      <span class="visually-hidden">unread messages</span>
    </span>
  </div>`

    // ________________________________________________________________

    modal = `<div class="offcanvas offcanvas-start" style="width: 28%;" tabindex="-1" id="modal` + hashIndexId + `"  data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1"  aria-labelledby="offcanvasScrollingLabel">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasExampleLabel">Offcanvas</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">`


    const editHtml = canvasZone.innerHTML + `<div id="component-` + hashIndexId + `"><content id="contend-` + hashIndexId + `">` + list1.getAttribute('html') + `</content>` + buttonEdit;
    canvasZone.innerHTML = editHtml + dropper

    text = ""
    getChild(`contend-` + hashIndexId)
    console.log(text)

    modal += text


    modal += `<button class="btn btn-danger" onclick="del('modal` + hashIndexId + `', 'component-` + hashIndexId + `')">Delete</button>`

    modal += `
    </div>
  </div>`


    // ________________________________________________________________



    const modalsSection = document.getElementById('modals').innerHTML;
    document.getElementById('modals').innerHTML = modalsSection + modal;


    eval(list1.getAttribute('js'));
    document.getElementById('value').value = editHtml
  }
}

function changeInp(id, inpid) {
  document.getElementById(id).innerHTML = document.getElementById(inpid).value
  document.getElementById(inpid).setAttribute("value", document.getElementById(inpid).value);
}

function changeInpImg(id, inpid) {
  document.getElementById(id).src = document.getElementById(inpid).value
  document.getElementById(inpid).setAttribute("value", document.getElementById(id).src);
}

function changeInput(id, inpid) {
  document.getElementById(id).placeholder = document.getElementById(inpid).value
  document.getElementById(inpid).setAttribute("value", document.getElementById(id).placeholder);
}

function changeInputHref(id, inpid) {
  document.getElementById(id).setAttribute("href", document.getElementById(inpid).value);
  document.getElementById(inpid).setAttribute("value", document.getElementById(id).getAttribute('href'));
}


function getChild(divId) {
  const childs = document.getElementById(divId).children;
  divNum += 1;
  for (let i = 0; i < childs.length; i++) {
    if (childs[i].id == '') {
      childs[i].id = randomIdFun();
    }
    getChild(childs[i].id);
  }
  const tn = document.getElementById(divId).tagName
  if (tn == 'P' || tn == 'H1' || tn == 'H2' || tn == 'H3' || tn == 'H4' || tn == 'H5' || tn == 'H6' || tn == 'BUTTON') {
    innerhtm = document.getElementById(divId);
    text += `<div class="input-group input-group-sm mb-3">
    <span class="input-group-text bg-info text-light" id="basic-addon1">` + tn + `</span>
    <input class="form-control" aria-describedby="basic-addon1" id="`+ `input` + innerhtm.id + `" type="text" value='` + innerhtm.innerHTML + `' onchange="changeInp('` + innerhtm.id + `', 'input` + innerhtm.id + `')">
  </div>`;
  } else if (tn == 'IMG') {
    innerhtm = document.getElementById(divId);
    text += `<div class="input-group mb-3">
    <span class="input-group-text bg-success text-light" id="basic-addon1">` + tn + `</span>
    <input class="form-control" aria-describedby="basic-addon1" id="`+ `input` + innerhtm.id + `" type="text" value='` + innerhtm.getAttribute('src') + `' onchange="changeInpImg('` + innerhtm.id + `', 'input` + innerhtm.id + `')">
    </div>`;
  }else if (tn == 'INPUT') {
    innerhtm = document.getElementById(divId);
    text += `<div class="input-group mb-3">
    <span class="input-group-text bg-warning text-light" id="basic-addon1">` + tn + `</span>
    <input class="form-control" aria-describedby="basic-addon1" id="`+ `input` + innerhtm.id + `" type="text" value='` + innerhtm.placeholder + `' onchange="changeInput('` + innerhtm.id + `', 'input` + innerhtm.id + `')">
    </div>`;
  }else if (tn == 'A') {
    innerhtm = document.getElementById(divId);
    text += `<div class="input-group mb-3">
    <span class="input-group-text bg-primary text-light" id="basic-addon1">` + tn + `</span>
      <input type="text" aria-label="First name" class="form-control"
      id="input` + innerhtm.id + `" 
      type="text" 
      value='` + innerhtm.innerHTML + `' 
      onchange="changeInp('` + innerhtm.id + `', 'input` + innerhtm.id + `')">

      <input type="text" aria-label="Last name" class="form-control"
      id="`+ `input1` + innerhtm.id + `" 
      type="text" 
      value='` + innerhtm.getAttribute('href') + `' 
      onchange="changeInputHref('` + innerhtm.id + `', 'input1` + innerhtm.id + `')">

    </div>`;
  }
}

function randomIdFun() {
  randomId++;
  const d = new Date();
  return CryptoJS.MD5("id" + d + randomId);
}