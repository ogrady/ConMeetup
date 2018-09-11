<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="ConMeetup">
	<meta name="author" content="datamate">
	<link rel="icon" href="/static/favicon.ico">		
	<title>ConMeetup</title>
	<link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
	<script type="text/javascript" src="/static/jquery.min.js"></script>
	<script type="text/javascript" src="/static/bootstrap.min.js"></script>
	<script type="text/javascript" src="/static/tablesorter.min.js"></script>
	<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery-validation@1.17.0/dist/jquery.validate.min.js"></script>
</head>
<body>
	<!-- Static navbar -->
	<nav class="navbar navbar-default navbar-static-top">
		<div class="container">
			<div class="row">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="#">Convention Meetup</a>
				</div>
				<div id="navbar" class="navbar-collapse collapse">
					<ul class="nav navbar-nav navbar-right">
						<li><a href="registration">Create Group</a></li>
						<li><a href="join">Join Group</a></li>
					</ul>
				</div><!--/.nav-collapse -->
			</div>
		</div>
	</nav>
	<div class="container">
		<div class="row">
			<div class="jumbotron">
			{{!base}}
			</div>
		</div>
		<!--./row-->
		<div class="row">
			<hr>
			<footer>
				<p>&copy; {{data["year"]}} {{data["developer_organization"]}}.</p>
			</footer>			
		</div>
	</div> 
	<!-- /container -->

<!-- Modal -->
  <div class="modal fade" id="modal" role="dialog">
    <div class="modal-dialog modal-sm">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">Modal Header</h4>
        </div>
        <div class="modal-body">
          <p>This is a small modal.</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Schließen</button>
        </div>
      </div>
    </div>
  </div>
</body>
</html>