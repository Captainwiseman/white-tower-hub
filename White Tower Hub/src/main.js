import App from './App.svelte';

const app = new App({
	target: document.body
	// Future props: 
	// props: {
	// 	propKey: `propValue`
	// }
});

window.app = app;

export default app;