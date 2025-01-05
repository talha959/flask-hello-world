from flask import Blueprint

blueprint = Blueprint('filters', __name__)

@blueprint.app_template_filter('nl2br')
def nl2br(value):
    """Convert newlines to HTML line breaks."""
    if not value:
        return value
    return value.replace('\n', '<br>')