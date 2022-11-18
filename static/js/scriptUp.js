componentIndex = -1;
randomId = -1

function allowDrop(ev) { ev.preventDefault() }
function drag(ev) { ev.dataTransfer.setData('text', ev.target.id) }

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
    const hashIndexId = CryptoJS.MD5("" + componentIndex);


    // ________________________________________________________________

    modal = `<div class="modal fade" id="modal` + hashIndexId + `" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">`

    modal += componentIndex

    modal += `</div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>`


    // ________________________________________________________________

    buttonEdit = `<span style="z-index: 2; left:64%;" class="position-absolute top-25 translate-middle badge">
      <button class="btn btn-primary px-5 py-1 rounded-pill bg-gradient text-white" data-bs-toggle="modal" data-bs-target="#modal`+ hashIndexId + `">Edit</button>
      <span class="visually-hidden">unread messages</span>
    </span>
  </div>`

    // ________________________________________________________________

    const editHtml = canvasZone.innerHTML + `<div id="component-` + hashIndexId + `"><content id="contend-` + hashIndexId + `">` + list1.getAttribute('html') + `</content>` + buttonEdit;
    canvasZone.innerHTML = editHtml + dropper

    text = ""
    getChild(`contend-` + hashIndexId)
    alert(text)

    const modalsSection = document.getElementById('modals').innerHTML;
    document.getElementById('modals').innerHTML = modalsSection + modal;


    eval(list1.getAttribute('js'));
    document.getElementById('value').value = editHtml
  }
}

  
function getChild(divId) {
  const htmlNowDragObj = document.getElementById(divId).children;
  for (let i = 0; i < htmlNowDragObj.length; i++) {
    text += htmlNowDragObj[i].tagName + ">";
    console.log(htmlNowDragObj[i].children)
    childs = htmlNowDragObj[i].children;
    if (childs.length > 0) {
      for (let j = 0; j < childs.length; j++) {
        if(childs[j].id == ''){
          childs[j].id = randomIdFun();
          getChild(childs[j].id);
        }
        else
          getChild(childs[j].id);
      }
    }
  }
}

function randomIdFun(){
  randomId ++;
  return CryptoJS.MD5("id" + randomId);
}