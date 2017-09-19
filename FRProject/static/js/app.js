        var f = 0; 
	var formSubmit = function(){
		if(f==1)
			document.getElementById('form').submit();	
	}
	
	document.onreadystatechange=function() {
              $('[data-toggle="tooltip"]').tooltip(); 
        
       	      var holder = document.getElementById('holder');
              holder.ondragover = function () { this.className = 'hover'; return false; };    
              holder.ondrop = drop;
              function drop(e) {
                e.preventDefault();
                var file = e.dataTransfer.files[0];
		var reader = new FileReader();
                reader.onload = function () {
       		       document.getElementById('output_image').src=reader.result;
                       document.getElementById('fname').innerHTML =""
                       document.getElementById('hname').innerHTML="";
                       document.getElementById('pbar').innerHTML="";
                       document.getElementById('d2').style.display = 'none';
                       document.getElementById('d1').style.display = 'block';
      		       document.getElementById('t1').value = reader.result+"#"+file.name;
		       f = 1;
                }
                reader.readAsDataURL(file);
              };
	};
        
        var load = function(event){
                var reader = new FileReader();
                reader.onload = function(){
                       document.getElementById('d2').style.display = 'none';
                       document.getElementById('d1').style.display = 'block';
                       document.getElementById('output_image').src = reader.result;
                       document.getElementById('fname').innerHTML = document.getElementById('file1').value.split('\\')[2].split('.')[0];
                       document.getElementById('hname').innerHTML="";
                       document.getElementById('pbar').innerHTML="";
	               f = 1;
                }
                reader.readAsDataURL(event.target.files[0]); 
        };

	 var video = document.querySelector('video');
	
	 function takeSnapshot() {
                document.getElementById('output_image').style.display = 'block';
                document.getElementById('v1').style.display = 'none';
	      var img =  document.createElement('output_image');
	      var context;
	      var width = video.offsetWidth
	        , height = video.offsetHeight;

	      var canvas =document.createElement('canvas');
	      canvas.width = width;
	      canvas.height = height;

	      context = canvas.getContext('2d');
	      context.drawImage(video, 0, 0, width, height);

	      img.src = canvas.toDataURL('image/png');
	  }

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
window.URL = window.URL || window.webkitURL || window.mozURL || window.msURL;

function successCallback(stream) {
    if (video.mozSrcObject !== undefined) {
        video.mozSrcObject = stream;
    } else {
        video.src = (window.URL && window.URL.createObjectURL(stream)) || stream;
    };
    var playPromise = document.getElelementById('v1').play();

    if (playPromise !== undefined) {
         playPromise.then(function() {
        }).catch(function(error) {
        });
}

//video.addEventListener('click', takeSnapshot);
}

function errorCallback(error) {
        console.error('An error occurred: [CODE ' + error.code + ']');
        // Display a friendly "sorry" message to the user
    }


	var startCamera = function(){
		
                document.getElementById('output_image').style.display = 'none';
                document.getElementById('v1').style.display = 'block';
   		
        if (navigator.getUserMedia) {
                navigator.getUserMedia({video: true}, successCallback, errorCallback);
        }

        else{
                console.log('Native device media streaming (getUserMedia) not supported in this browser.');
        }


	 };
