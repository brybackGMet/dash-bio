# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Jsme(Component):
    """A Jsme component.
JSME is a molecule editor that supports drawing and
editing of molecules and reactions on in a web app,
supporting both desktop and mobile devices. A built-in
substituent menu and several keyboard shortcuts
provide speedy access to the most common editing features and allow easy
and fast creation of even large and complex molecules. The editor
is able to export molecules as SMILES, MDL/Symyx/Accelrys Molfile or
in its own compact format (one line textual representation of a molecule or
reaction including also atomic 2D coordinates). The SMILES code generated by the JSME
is canonical, i.e. independent on the way how the molecule was drawn.

See more detailed documentation here: https://jsme-editor.github.io/help.html

Keyword arguments:

- id (string; default 'jsme'):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- eventSmiles (string; optional):
    A Dash prop that returns data when SMILE will be changed.

- height (string; default '600px'):
    The height of the JSME container. Can be set in px, % etc.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- options (string; default 'newLook'):
    String that is a comma separated string of JSME options. The
    available options are described on the
    https://wiki.jmol.org/index.php/Jmol_JavaScript_Object/JME/Options.

- smiles (string; optional):
    The molecule SMILE to display.

- style (dict; optional):
    Generic style overrides on the plot div.

- width (string; default '600px'):
    The width of the JSME container. Can be set in px, % etc."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, options=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, eventSmiles=Component.UNDEFINED, smiles=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'eventSmiles', 'height', 'loading_state', 'options', 'smiles', 'style', 'width']
        self._type = 'Jsme'
        self._namespace = 'dash_bio'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'eventSmiles', 'height', 'loading_state', 'options', 'smiles', 'style', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Jsme, self).__init__(**args)
