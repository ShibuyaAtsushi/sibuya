// main.js
let scene, camera, renderer, cube;

function init() {
  // シーンの作成
  scene = new THREE.Scene();

  // カメラの作成
  camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  camera.position.z = 5;

  // レンダラーの作成
  renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  // 立方体の作成
  const geometry = new THREE.BoxGeometry();
  const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
  cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  // アニメーションの開始
  animate();
}

function animate() {
  requestAnimationFrame(animate);

  // 立方体の回転
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;

  // カメラの周りを円状に移動
  const time = Date.now() * 0.0005;
  camera.position.x = Math.sin(time) * 5;
  camera.position.z = Math.cos(time) * 5;
  camera.lookAt(scene.position);

  // レンダリング
  renderer.render(scene, camera);
}

// ウィンドウのリサイズ時にカメラやレンダラーを更新
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// 初期化
init();
