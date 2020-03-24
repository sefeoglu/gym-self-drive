'''
Sefika Efeoglu
'''
import tensorflow as tf
import numpy as np
import glob, random, os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class VariationalAutoencoderConfigBase(object):
    '''Configuration General Class'''
    def __init__(self):
        pass
    def sample_z(self, mu, logvar):
        eps = tf.random_normal(shape=tf.shape(mu))
        return mu + tf.exp(logvar / 2) * eps

    def compute_loss(self, reconstructions, resized_image, z_mu, z_logvar):
        
        logits_flat = tf.keras.layers.Flatten()(reconstructions)
        labels_flat = tf.keras.layers.Flatten()(resized_image)
        reconstruction_loss = tf.reduce_sum(tf.square(logits_flat - labels_flat), axis = 1)
        kl_loss = 0.5 * tf.reduce_sum(tf.exp(z_logvar) + z_mu**2 - 1. - z_logvar, 1)
        vae_loss = tf.reduce_mean(reconstruction_loss + kl_loss)
        return vae_loss

    def encoder(self, x, filter_list):
        x = tf.keras.layers.Conv2D(filters=filter_list[0], kernel_size=4, strides=2, padding='valid', activation=tf.nn.relu)(x)
        x = tf.keras.layers.Conv2D(filters=filter_list[1], kernel_size=4, strides=2, padding='valid', activation=tf.nn.relu)(x)
        x = tf.keras.layers.Conv2D(filters=filter_list[2], kernel_size=4, strides=2, padding='valid', activation=tf.nn.relu)(x)
        x = tf.keras.layers.Conv2D(filters=filter_list[3], kernel_size=4, strides=2, padding='valid', activation=tf.nn.relu)(x)

        x = tf.keras.layers.Flatten()(x)
        z_mu = tf.keras.layers.Dense(units=32, name='z_mu')(x)
        z_logvar = tf.keras.layers.Dense( units=32, name='z_logvar')(x)
        return z_mu, z_logvar

    def decoder(self, z, filter_list):
        x = tf.keras.layers.Dense(1024, activation=None)(z)
        x = tf.reshape(x, [-1, 1, 1, 1024])
        x = tf.keras.layers.Conv2DTranspose(filters=filter_list[0], kernel_size=5, strides=2, padding='valid', activation=tf.nn.relu)(x)
        x = tf.keras.layers.Conv2DTranspose(filters=filter_list[1], kernel_size=5, strides=2, padding='valid', activation=tf.nn.relu)(x)
        x = tf.keras.layers.Conv2DTranspose(filters=filter_list[2], kernel_size=6, strides=2, padding='valid', activation=tf.nn.relu)(x)
        x = tf.keras.layers.Conv2DTranspose(filters=filter_list[3], kernel_size=6, strides=2, padding='valid', activation=tf.nn.sigmoid)(x)
        return x

class VariationalAutoencoderConfig1(VariationalAutoencoderConfigBase):
    '''VariationalAutoEncoder'''
    def __init__(self):
        self.image = tf.placeholder(tf.float32, [None, 96, 96, 3], name='image')
        self.resized_image = tf.image.resize_images(self.image, [64, 64])
        tf.summary.image('resized_image', self.resized_image, 20)
        self.encoder_filter = [32, 64, 128, 256]
        self.z_mu, self.z_logvar = super().encoder(self.resized_image, self.encoder_filter)
        self.z = super().sample_z(self.z_mu, self.z_logvar)
        self.decoder_filter = [128, 64, 32, 3]
        self.reconstructions = super().decoder(self.z, self.decoder_filter)
        tf.summary.image('reconstructions', self.reconstructions, 20)

        self.merged = tf.summary.merge_all()

        self.loss = super().compute_loss(self.reconstructions, self.resized_image, self.z_mu, self.z_logvar)

class VariationalAutoencoderConfig2(VariationalAutoencoderConfigBase):
    '''VariationalAutoEncoder'''
    def __init__(self):
        self.image = tf.placeholder(tf.float32, [None, 96, 96, 3], name='image')
        self.resized_image = tf.image.resize_images(self.image, [64, 64])
        tf.summary.image('resized_image', self.resized_image, 20)
        self.encoder_filter = [4, 8, 16, 32]
        self.z_mu, self.z_logvar = super().encoder(self.resized_image, self.encoder_filter)
        self.z = super().sample_z(self.z_mu, self.z_logvar)
        self.decoder_filter = [32, 16, 4, 3]
        self.reconstructions = super().decoder(self.z, self.decoder_filter)
        tf.summary.image('reconstructions', self.reconstructions, 20)

        self.merged = tf.summary.merge_all()

        self.loss = super().compute_loss(self.reconstructions, self.resized_image, self.z_mu, self.z_logvar)


class VariationalAutoencoderConfig3(VariationalAutoencoderConfigBase):
    '''VariationalAutoEncoder3'''
    def __init__(self):
        self.image = tf.placeholder(tf.float32, [None, 96, 96, 3], name='image')
        self.resized_image = tf.image.resize_images(self.image, [64, 64])
        tf.summary.image('resized_image', self.resized_image, 20)
        self.encoder_filter = [16, 32, 64, 128]
        self.z_mu, self.z_logvar = super().encoder(self.resized_image, self.encoder_filter)
        self.z = super().sample_z(self.z_mu, self.z_logvar)
        self.decoder_filter = [64, 32, 16, 3]
        self.reconstructions = super().decoder(self.z, self.decoder_filter)
        tf.summary.image('reconstructions', self.reconstructions, 20)

        self.merged = tf.summary.merge_all()

        self.loss = super().compute_loss(self.reconstructions, self.resized_image, self.z_mu, self.z_logvar)
   
class VariationalAutoencoderConfig4(VariationalAutoencoderConfigBase):
    '''VariationalAutoEncoder4'''
    def __init__(self):
        self.image = tf.placeholder(tf.float32, [None, 96, 96, 3], name='image')
        self.resized_image = tf.image.resize_images(self.image, [64, 64])
        tf.summary.image('resized_image', self.resized_image, 20)
        self.encoder_filter = [64, 128, 256, 512]
        self.z_mu, self.z_logvar = super().encoder(self.resized_image)
        self.z = super().sample_z(self.z_mu, self.z_logvar)
        self.decoder_filter = [256, 128, 64, 3]
        self.reconstructions = super().decoder(self.z, self.decoder_filter)
        tf.summary.image('reconstructions', self.reconstructions, 20)

        self.merged = tf.summary.merge_all()

        self.loss = super().compute_loss(self.reconstructions, self.resized_image, self.z_mu, self.z_logvar)