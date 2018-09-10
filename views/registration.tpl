% rebase('base.tpl')
<form class="needs-validation" id="formRegistration" action="ajax/register" method="POST">
  <h3>Group Data</h3>
  <div class="form-group">
    <label for="inpPassword">Group Password</label>
    <input type="password" class="form-control" name="inpPassword" placeholder="Password" aria-describedby="passwordHelp" required>
    <small id="passwordHelp" class="form-text text-muted">Password to join your group with.</small>
  </div>
  <div class="form-group">
    <label for="inpFloorplan">Floor Plan</label>
    <input type="file" class="form-control" name="inpFloorplan" aria-describedby="floorplanHelp" required multiple>
    <small id="floorplanHelp" class="form-text text-muted">Image of the floor plan of the convention.</small>
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
<script>
  $(document).ready(function() {
    function handleImage(e){
        var reader = new FileReader();
        reader.onload = function(event){
            var img = new Image();
            img.onload = function(){
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(img,0,0);
            }
            img.src = event.target.result;
        }
        reader.readAsDataURL(e.target.files[0]);     
      } 
  });
</script>