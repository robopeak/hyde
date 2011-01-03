# -*- coding: utf-8 -*-
"""
Contains definition for a plugin protocol and other utiltities.
"""
import abc
from hyde import loader

class Plugin(object):
    """
    The plugin protocol
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, site):
        super(Plugin, self).__init__()
        self.site = site

    def template_loaded(self, template):
        """
        Called when the template for the site has been identified.
        """
        pass

    def begin_generation(self):
        """
        Called when generation is about to take place.
        """
        pass

    def begin_site(self):
        """
        Called when the site is loaded completely. This implies that all the
        nodes and resources have been identified and are accessible in the
        site variable.
        """
        pass

    def begin_node(self, node):
        """
        Called when a node is about to be processed for generation.
        This method is called only when the entire node is generated.
        """
        pass

    def begin_text_resource(self, resource, text):
        """
        Called when a text resource is about to be processed for generation.
        The `text` parameter contains the resource text at this point
        in its lifecycle. It is the text that has been loaded and any
        plugins that are higher in the order may have tampered with it.
        But the text has not been processed by the template yet. Note that
        the source file associated with the text resource may not be modifed
        by any plugins.

        If this function returns a value, it is used as the text for further
        processing.
        """
        return text

    def begin_binary_resource(self, resource):
        """
        Called when a binary resource is about to be processed for generation.

        Plugins are free to modify the contents of the file.
        """
        pass

    def text_resource_complete(self, resource, text):
        """
        Called when a resource has been processed by the template.
        The `text` parameter contains the resource text at this point
        in its lifecycle. It is the text that has been processed by the
        template and any plugins that are higher in the order may have
        tampered with it. Note that the source file associated with the
        text resource may not be modifed by any plugins.

        If this function returns a value, it is used as the text for further
        processing.
        """
        return text

    def binary_resource_complete(self, resource):
        """
        Called when a binary resource has already been processed.

        Plugins are free to modify the contents of the file.
        """
        pass

    def node_complete(self, node):
        """
        Called when all the resources in the node have been processed.
        This method is called only when the entire node is generated.
        """
        pass

    def site_complete(self):
        """
        Called when the entire site has been processed. This method is called
        only when the entire site is generated.
        """
        pass

    def site_complete(self):
        """
        Called when the generation process is complete. This method is called
        only when the entire site is generated.
        """
        pass

    def generation_complete(self):
        """
        Called when generation is completed.
        """
        pass

    @staticmethod
    def load_all(site):
        """
        Loads plugins based on the configuration. Assigns the plugins to
        'site.plugins'
        """

        site.plugins = [loader.load_python_object(name)(site)
                            for name in site.config.plugins]