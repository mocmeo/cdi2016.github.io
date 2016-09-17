from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<footer id="footer" role="contentinfo">


		<div class="container">

			<div class="col-md-3 company-details"><div class="icon-top red-text"><img src="http://www.bbg.com.vn/wp-content/themes/zerif-lite/images/map25-redish.png" alt="" /></div><div class="zerif-footer-address">Khu X98, Ngõ 97 Hoàng Cầu, Đống Đa, Hà Nội </div></div><div class="col-md-3 company-details"><div class="icon-top green-text"><img src="http://www.bbg.com.vn/wp-content/themes/zerif-lite/images/envelope4-green.png" alt="" /></div><div class="zerif-footer-email"><a href="mailto:contact@bbg.com.vn">contact@bbg.com.vn</a></div></div><div class="col-md-3 company-details"><div class="icon-top blue-text"><img src="http://www.bbg.com.vn/wp-content/themes/zerif-lite/images/telephone65-blue.png" alt="" /></div><div class="zerif-footer-phone"><a href="tel:09 04 953 962">09 04 953 962</a></div></div><div class="col-md-3 copyright"><ul class="social"><li><a target="_blank" href="https://www.facebook.com/bluebirdaward"><i class="fa fa-facebook"></i></a></li><li><a target="_blank" href="#"><i class="fa fa-twitter"></i></a></li><li><a target="_blank" href="#"><i class="fa fa-linkedin"></i></a></li><li><a target="_blank" href="#"><i class="fa fa-behance"></i></a></li><li><a target="_blank" href="#"><i class="fa fa-dribbble"></i></a></li></ul><p id="zerif-copyright">Bluebird Award 2016</p><div class="zerif-copyright-box"><a class="zerif-copyright" href="http://themeisle.com/themes/zerif-lite/" target="_blank" rel="nofollow">Zerif Lite </a>powered by<a class="zerif-copyright" href="http://wordpress.org/" target="_blank" rel="nofollow"> WordPress</a></div></div>
		</div> <!-- / END CONTAINER -->

	</footer> <!-- / END FOOOTER  -->
</body>
</html>

"""
soup = BeautifulSoup(html_doc, 'html.parser')

with open("abc.html", 'w') as f:
	f.write(soup.prettify())
