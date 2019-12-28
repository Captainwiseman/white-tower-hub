<script>
    // Possible Idea:
    // Change the entire nav system for the sidebar to be more visually.
    // Meaning the entire menu logic is managed in the App.sevelte, giving props to the sidebar for which menu item to render (category/nav items).
    // That way the logic of the items are on master and being handled through one main source across the app

    import NavButton from './NavButton.svelte'
    import {createEventDispatcher} from 'svelte';
    const dispatch = createEventDispatcher();

    let navButtons = {
        dashboard: {
            active: true
        },
        msgboard: {
            active: false
        }
    }

    const changeActiveTab = (event) => {
        if (event.detail.shouldChangeActiveTab) {
            const tabToSwitchTo = event.detail.tabId

            for (let navButton in navButtons) {
                navButtons[navButton].active = false
            }
            navButtons[tabToSwitchTo].active = !navButtons[tabToSwitchTo].active
            console.log("Sidebar got a request to change the tab to", tabToSwitchTo)
            dispatch("navClick", {
                shouldChangeActiveTab: tabToSwitchTo
            })
        } else if (event.detail.shouldRefreshActiveTabshouldRefreshActiveTab) {
            console.log("Sidebar got a request to refresh current tab")
            dispatch("navClick", {
                shouldRefreshActiveTab: true
            })
        }

    }
</script>

<!-- Sidebar -->
<ul class="navbar-nav bg-gradient-dark sidebar sidebar-dark accordion" id="accordionSidebar">

    <!-- Sidebar - Brand -->
    <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.html">
        <div class="sidebar-brand-icon">
            <i class="fas fa-gopuram"></i>
        </div>
        <div class="sidebar-brand-text mx-3">White Tower Hub</div>
    </a>

    <!-- Divider -->
    <hr class="sidebar-divider my-0">

    <!-- Nav Item - Dashboard -->
    <NavButton title="Dashboard" active={navButtons.dashboard.active} tabId="dashboard"
        iconClass="fas fa-fw fa-tachometer-alt" on:navClick={changeActiveTab} />

    <!-- Divider -->
    <hr class="sidebar-divider">

    <!-- Heading -->
    <div class="sidebar-heading">
        Social
    </div>

    <!-- Nav Item - Pages Collapse Menu -->
    <NavButton title="Message Board" active={navButtons.msgboard.active} tabId="msgboard" iconClass="far fa-comments"
        on:navClick={changeActiveTab} />

    <!-- Divider -->
    <hr class="sidebar-divider">

</ul>
<!-- End of Sidebar -->