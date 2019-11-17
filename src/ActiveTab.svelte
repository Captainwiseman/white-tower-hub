<!-- Importing App Pages -->
<script>
    import Dashboard from './Tabs/Dashboard';
    import Msgboard from './Tabs/Msgboard';
    
    const tabs = {
        dashboard: {
            component: Dashboard
        },
        msgboard: { 
            component: Msgboard
        }
    }
    export let currentTab = tabs[dashboard].component
    $: activeTab = tabs[currentTab].component

</script>

<!-- Begin Page Content -->
<div class="container-fluid">
    <svelte:component this={activeTab}/>
</div>

<!-- /.container-fluid -->