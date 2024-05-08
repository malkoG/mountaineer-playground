from mountaineer.app import AppController
from mountaineer.js_compiler.postcss import PostCSSBundler
from mountaineer.render import LinkAttribute, Metadata


from mountaineer_playground.controllers.detail import DetailController
from mountaineer_playground.controllers.home import HomeController

from mountaineer_playground.config import AppConfig

controller = AppController(
    config=AppConfig(), # type: ignore
    
    global_metadata=Metadata(
        links=[LinkAttribute(rel="stylesheet", href="/static/app_main.css")]
    ),
    custom_builders=[
        PostCSSBundler(),
    ],
    
)


controller.register(HomeController())
controller.register(DetailController())
