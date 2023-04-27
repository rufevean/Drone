import * as THREE from "C:/code/Drone/node_modules/three/src/Three.js";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

// making a drone object


let drone = {
    el: document.getElementById("drone"),
    scene: null,
    renderer: null,
    camera: null,
    position: null,
};



const init = () => {
    // creating a scene
    drone.scene = new THREE.Scene();
    drone.scene.background = new THREE.Color("gray"); // Set background color
    drone.camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        10000
    );
    drone.camera.position.set(0, 10, 0);
    drone.camera.lookAt(drone.scene.position);
    drone.scene.position.set(0, 0, 0);
    drone.scene.rotation.set(2.5, 0, 2.9);

    drone.renderer = new THREE.WebGLRenderer();
    drone.renderer.physicallyCorrectLights = true;
    drone.renderer.setSize(window.innerWidth/2, window.innerHeight/2);
    drone.el.appendChild(drone.renderer.domElement);

    //orbital controls
    const controls = new OrbitControls(drone.camera, drone.renderer.domElement);
    controls.enableDamping = true;
    controls.enableZoom = false;
    controls.enablePan = false;
    controls.enableRotate = false;
    drone.renderer.gammaInput = true;
    drone.renderer.gammaOutput = true;
    
    // Add directional lighting
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(0, 100, 0);
    drone.scene.add(light);

    const light2 = new THREE.DirectionalLight(0xffffff, 1);
    light2.position.set(0, -100, 0);
    drone.scene.add(light2);

    const light3 = new THREE.DirectionalLight(0xffffff, 0.5);
    light3.position.set(100, 0, 0);
    drone.scene.add(light3);

    const light4 = new THREE.DirectionalLight(0xffffff, 0.5);
    light4.position.set(-100, 0, 0);
    drone.scene.add(light4);

    const light5 = new THREE.DirectionalLight(0xffffff, 0.5);
    light5.position.set(0, 0, 100);
    drone.scene.add(light5);

    const light6 = new THREE.DirectionalLight(0xffffff, 0.5);
    light6.position.set(0, 0, -100);
    drone.scene.add(light6);

    // Add ambient lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.3);
    drone.scene.add(ambientLight);

    // Add hemisphere lighting
    const hemiLight = new THREE.HemisphereLight(0xffffff, 0xffffff, 0.6);
    hemiLight.position.set(0, 200, 0);
    drone.scene.add(hemiLight);

    // const axesHelper = new THREE.AxesHelper(5);
    // drone.scene.add(axesHelper);
};

const render = () => {
    drone.renderer.render(drone.scene, drone.camera);
};

// uncomment later

const loader = new GLTFLoader();

loader.load(
    "dji_mavic_air_drone/scene.gltf",
    function (gltf) {
        console.log(gltf.scene);
        gltf.scene.scale.set(.4, .4 ,.4);
        gltf.scene.position.set(0, 0, 0);
        drone.scene.add(gltf.scene);
        // const xRotation = - Math.PI / 4; // rotates 45 degrees
        // gltf.scene.rotation.x = xRotation;

        const box = new THREE.Box3().setFromObject(gltf.scene);
        const size = new THREE.Vector3();
        box.getSize(size);
        console.log("Size of the object:", size.x, size.y, size.z);
    },
    undefined,
    function (error) {
        console.error(error);
    }
);
const animate = () => {
    const currentRotation = drone.scene.rotation.clone();

    // calculate the new Y-axis rotation
    const newYRotation = currentRotation.y + 0.01;

    // set the new rotation of the drone
    drone.scene.rotation.set(currentRotation.x, newYRotation ,currentRotation.z);
    

    requestAnimationFrame(animate);
    render();
};

init();
animate();
