Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL),
  faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL),
  faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
  faceapi.nets.faceExpressionNet.loadFromUri(MODEL_URL),
]);

async function doMagic() {
  if (context.is_doctor == "true") {
    const parent_div = document.querySelector('.magic-container');
    const patient_view = parent_div.lastChild;
    var input = '';

    var children = patient_view.children;
    for (let index = 0; index < children.length; index++) {
        const element = children[index];
        if(element.tagName == 'VIDEO'){
          // add class to the element, make the class position relative and make the canvas absolute, probably make the canvas a child of the magic container?
            input = element;
        }
    }
    console.log(input);
    // const input = patient_view.lastChild;
    input.setAttribute("id", "patient_video");
    const video = document.getElementById("patient_video");
    detectFaces(video);
  } else {
    console.log("not a doctor");
  }
};

function waitForElm(selector) {
  return new Promise((resolve) => {
    if (document.querySelector(selector)) {
      return resolve(document.querySelector(selector));
    }

    const observer = new MutationObserver((mutations) => {
      if (document.querySelector(selector)) {
        resolve(document.querySelector(selector));
        observer.disconnect();
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true,
    });
  });
}

function detectFaces(input) {
  const canvas = faceapi.createCanvasFromMedia(input);
  document.body.append(canvas);
  const displaySize = { width: input.videoWidth, height: input.videoHeight };
  faceapi.matchDimensions(canvas, displaySize);
  setInterval(async () => {
    const detections = await faceapi
      .detectAllFaces(input, new faceapi.TinyFaceDetectorOptions())
      .withFaceExpressions();
    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
    faceapi.draw.drawDetections(canvas, resizedDetections);
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections);
  }, 500);
}
