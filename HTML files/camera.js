const cameraFeed = document.getElementById('cameraFeed');
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        cameraFeed.srcObject = stream;
    })
    .catch(Error=>{
        console.error("error accesing camera:", error);
    })
