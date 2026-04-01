<script>
  import Router from 'svelte-spa-router';
  import Homepage from './lib/Homepage.svelte';
  import Signup from './lib/Signup.svelte';
  import Login from './lib/Login.svelte';
  import SignupLoginSwitch from './lib/Signup_Login_Switch.svelte';
  import NavBar from './lib/NavBar.svelte';
  import ChatInterface from './lib/ChatInterface.svelte';

  const routes = {
    '/homepage': Homepage,
    '/signup': Signup,
    '/login': Login,
    '/chat': NavBar,

    '*': Login
  }
</script>

<div>
  <!-- <div>
    <NavBar></NavBar>
  </div> -->
  <div>
    <Router {routes} />
  </div>
  <SignupLoginSwitch></SignupLoginSwitch>
</div>
<!-- <ChatInterface></ChatInterface> -->