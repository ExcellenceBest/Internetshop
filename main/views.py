from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    return HttpResponse(
        """  <header>
    <nav class="navbar navbar-expand-lg bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="/"><img src="Source/images/logo.jpg" alt="..."></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/">Дизайн ногтей</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="pricing.html">Маникюр</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="pricing.html">Педикюр</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="pricing.html">Наша команда</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="pricing.html">Контакты</a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <a title="Telegram" href="https://telegram.me/VladimirElsukov" target="_blank"><img style="width: 35px; margin-inline: 1em;"
                  src="Source/images/tg.png" alt="Написать в Telegram" /></a>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link"">
                <img style=" width: 45px; margin-inline: 1em; margin-top: 0.5em;" src="Source/images/yt.png" alt="...">
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link"">
                <a href=" https://api.whatsapp.com/send?phone=79806554191" target="_blank" title="Написать в Whatsapp"
                rel="noopener noreferrer">
                <div class="whatsapp-button"><i class="fa fa-whatsapp"></i></div>
              </a>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>"""
    )
