class Urlcode

  OFFSET = 0

  def self.uuid_to_code(uuid)
    # Get each character code
    bytes = uuid.gsub('-','').split('').map do |char|
      charcode(char)
    end
    # Map into a single binary string map
    bitmap = bytes.map{|b|
      str = b.to_s(2)
      while str.length < 4
        str = "0" + str
      end
      str
    }

    chunkmap = bitmap.join('').scan(/.{1,16}/)

    unicodemap = chunkmap.map do |chunk|
      (chunk.to_i(2)+OFFSET).chr
    end.join('').encode("UTF-8")
  end

  def self.code_to_uuid(string)
    bitmap = []
    string.each_codepoint do |code|
      map = []
      str = (code - OFFSET).to_s(2)
      while str.length < 16
        str = "0" + str
      end
      bitmap << (str)
    end

    chunkmap = bitmap.join('').scan(/.{1,4}/)
    out = chunkmap.map do |chunk|
      code = chunk.to_i(2)
      if code < 10
        (code + 48).chr
      else
        (code + 87).chr
      end
    end.
      join('').
      # Match the uuid portions and add the dashes back in
      scan(/([0-9a-f]{8})([0-9a-f]{4})([0-9a-f]{4})([0-9a-f]{4})([0-9a-f]{12})/).
      first.
      join('-')
  end

  private

  # Custom hex character set
  # 0-9a-f
  def self.charcode(char)
    if char.match(/[0-9]/)
      char.each_byte.first - 48
    elsif char.match(/[a-f]/)
      char.each_byte.first - 87
    else
      raise "Only 0-9 and a-f supported"
    end
  end
end
