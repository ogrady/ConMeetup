% rebase('base.tpl')
<form class="needs-validation" id="formRegister" action="ajax/register" method="POST" enctype="multipart/form-data">
  <h3>Group Data</h3>
  <div class="form-group">
    <label for="inpName">Group Name</label>
    <input type="text" class="form-control" name="inpName" placeholder="Group Name" aria-describedby="groupHelp" required>
    <small id="groupHelp" class="form-text text-muted">Please choose a unique name.</small>
  </div>
  <div class="form-group">
    <label for="inpPassword">Group Password</label>
    <input type="password" class="form-control" name="inpPassword" placeholder="Password" aria-describedby="passwordHelp" required>
    <small id="passwordHelp" class="form-text text-muted">Password to join your group with.</small>
  </div>
  <div class="form-group">
    <label for="inpFloorplan">Floor Plan</label>
    <input type="file" class="form-control" name="inpFloorplans" id="inpFloorplans" aria-describedby="floorplanHelp" required multiple>
    <small id="floorplanHelp" class="form-text text-muted">Image(s) of the floor plan of the convention.</small>
  </div>
  <div class="form-check">
    <label class="form-check-label">
      <input name="cbDSGVO" type="checkbox" aria-describedby="dsgvoHelp" class="form-check-input" required>
      I agree to the <a href="www.google.de">privacy policy</a>.
    </label>
    <small id="dsgvoHelp" class="form-text text-muted"></small>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
<button id="foobar">clickme</button>

<canvas id="canvas"></canvas>
<script>
  $(document).ready(function() {

  $("#formRegister").submit(function(event) {
    event.preventDefault();
    event.stopPropagation();
    console.log(this);
    $.ajax({
        url: this.action,
        type: "POST",
        data: new FormData(this),
        cache: false,
        contentType: false,
        processData: false
    });
  });

    $("#foobar").click(function(e) {
      e.preventDefault();
      let canvas = document.getElementById("canvas");
      let files = document.getElementById("inpFloorplan");
      let context = canvas.getContext("2d");
      var fr = new FileReader();
        fr.onload = function (e) {
          let img = new Image();
          console.log(img.width, img.height);
          img.src = fr.result;
          //canvas.width = img.width;
          //canvas.height = img.height;
          context.drawImage(img,0,0)
        }
        fr.readAsDataURL(files.files[0]);
    });
  });
</script>