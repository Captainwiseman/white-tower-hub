<script>
    export let active = false
    export let title
    export let linkToTab
    export let iconClass
    
    let navItemClass = "nav-item";
    if (active) {
        navItemClass = "nav-item active";
    }
    console.log(navItemClass)
    let changeTab = (tabId) => {
        console.log("need to redirect to:", tabId)
        if (active === false) {navItemClass = "nav-item active"}
    }
</script>

<li class={navItemClass}>
    <a class="nav-link" href="javascript:;" on:click={()=> changeTab(linkToTab)}>
        <i class={iconClass}></i>
        <span>{title}</span>
    </a>
</li>