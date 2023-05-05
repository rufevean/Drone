import 'C:/code/FromAbove-React/vite-project/src/styles/home.css';
import communityicon from 'C:/code/FromAbove-React/vite-project/src/components/assets/images/communityicon.png';
import newspapericon from  'C:/code/FromAbove-React/vite-project/src/components/assets/images/newspapericon.png';

function Home(){
    return(
		
        <body>
	<nav className="nav">
		<logo className="logo">
			<div className="logo-head">
				FromAbove
			</div>
			<div className="logo-tail">
				Discover the skies
			</div>
		</logo>
		<div className="nav-items">
			<div className="nav-community">
				<img alt="communityicon" className="nav-community-icon" src={communityicon}></img>
			</div>
			<div className="nav-news">
				<img alt="newspapericon" className="nav-news-icon" src={newspapericon}></img>
			</div>
			<div className="nav-menu">
				<hr></hr>
				<hr></hr>
			</div>
		</div>

	</nav>
	<section className="main-body">
		<div className="drone" id="drone">

		</div>

	</section>
	<footer className="footer">
	</footer>
</body>
    );
}

export default Home;