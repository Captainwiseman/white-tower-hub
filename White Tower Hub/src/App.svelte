<script>
	import Sidebar from './Sidebar';
	import Topbar from './Topbar';
	import ActiveTab from './ActiveTab'

	let currentTab = 'dashboard'

	const handleNavClick = (event) => {
		if (event.detail.changeTab) {
			currentTab = event.detail.changeTab
		}

	}
</script>
<main>
	<!-- Page Wrapper -->
	<div id="wrapper">

		<Sidebar on:navClick={handleNavClick} />

		<!-- Content Wrapper -->
		<div id="content-wrapper" class="d-flex flex-column">

			<!-- Main Content -->
			<div id="content">
				<Topbar />
				<ActiveTab currentTab={currentTab} />
			</div>
			<!-- End of Main Content -->

			<!-- Footer -->
			<footer class="sticky-footer bg-white">
				<div class="container my-auto">
					<div class="copyright text-center my-auto">
						<span>White Tower 2019</span>
					</div>
				</div>
			</footer>
			<!-- End of Footer -->

		</div>
		<!-- End of Content Wrapper -->

	</div>
	<!-- End of Page Wrapper -->

	<!-- Scroll to Top Button-->
	<a class="scroll-to-top rounded" href="#page-top">
		<i class="fas fa-angle-up"></i>
	</a>
</main>