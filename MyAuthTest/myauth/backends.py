import logging

#from myauth.models import MyUser
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class PasswordAuthBackend:
    def authenticate(self, username=None, password=None, token=None):
        """
        Authenticate the username/password, and return related 'User' object.
        Input:
        * credentials
        Output:
        * User object
        Mandatory: yes
        """
        logger.info("PasswordAuthBackend->authenticate(%s, %s) is called" %
                (username, password))
        user = None
        try:
            model = get_user_model()
            user = model.objects.get(username=username)
        except model.DoesNotExist:
            logger.error("User [%s] does not exist!" % username)
            user = None
        except Exception as e:
            logger.error("User [%s] authentication failure: %s" % e.message)
            user = None
        if user is not None:
            success = user.check_password(password)
            if not success:
                user = None
            else:
                logger.info("User [%s] is authenticated." % username)
        return user

    def get_user(self, user_id):
        """
        Input:
        * user_id
        Output:
        * User object
        Mandatory: yes
        """
        logger.info("PasswordAuthBackend->get_user(%d) is called" % user_id)
        try:
            model = get_user_model()
            user = model.objects.get(pk=user_id)
        except model.DoesNotExist:
            user = None
        return user
#
#    def has_perm(self, user, perm, obj=None):
#        logger.info("PasswordAuthBackend->has_perm() is called")
#        pass
#
#    def has_module_perms(self, user, app_label):
#        logger.info("PasswordAuthBackend->has_module_perms() is called")
#        pass
#
#    def get_all_permissions(self, user, obj=None):
#        logger.info("PasswordAuthBackend->get_all_permissions() is called")
#        pass
#
#    def get_group_permissions(self, user, obj=None):
#        logger.info("PasswordAuthBackend->get_group_permissions() is called")
#        pass


class TokenAuthBackend:
    def authenticate(self, token=None):
        """
        Authenticate the token, and return related 'User' object.
        """
        logger.info("TokenAuthBackend->authenticate() is called")
        return None

    def get_user(self, user_id):
        logger.info("TokenAuthBackend->get_user() is called")
        return None

    def has_perm(self, user, perm, obj=None):
        logger.info("TokenAuthBackend->has_perm() is called")
        pass

    def has_module_perms(self, user, app_label):
        logger.info("TokenAuthBackend->has_module_perms() is called")
        pass

    def get_all_permissions(self, user, obj=None):
        logger.info("TokenAuthBackend->get_all_permissions() is called")
        pass

    def get_group_permissions(self, user, obj=None):
        logger.info("TokenAuthBackend->get_group_permissions() is called")
        pass
